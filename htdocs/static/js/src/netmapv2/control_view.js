define([
    'netmap/collections',
    'netmap/models',
    'netmap/graph',
    'libs/backbone',
    'libs/backbone-eventbroker'
], function (Collections) {

    var ControlView = Backbone.View.extend({

        el: '#navigation-view',
        interests: {},
        events: {
            'submit #graph-search-form': 'searchGraph',
            'change #graph-layer-select': 'changeTopologyLayer',
            'change #graph-view-select': 'changeNetmapView',
            'click .filter-category': 'updateCategoryFilter',
            'click #filter-orphan-nodes': 'updateOrphanNodesFilter',
            'click #netmap-save-view': 'saveCurrentView',
            'click #netmap-view-panel-toggle': 'toggleNetmapViewPanel',
            'click #advanced-options-panel-toggle': 'toggleAdvancedOptionsPanel'
        },

        initialize: function () {

            // Initialize the available views from the
            // window-object.
            this.netmapViews = new Collections.NetmapViewCollection();
            this.netmapViews.reset(window.netmapData.views);
            this.currentView = this.netmapViews.get(window.netmapData.defaultView);

            this.initializeDOM();

            Backbone.EventBroker.register(this);
        },

        /**
         * Initializes and/or caches any necessary DOM elements.
         */
        initializeDOM: function () { // TODO: Consistent naming
            var self = this;

            this.netmapViewPanel = this.$('#netmap-view-panel');
            this.advancedOptionsPanel = this.$('#advanced-options-panel');
            this.alertContainer = this.$('#netmap-alert-container', this.netmapViewPanel);

            this.$('#graph-layer-select option').each(function (i, option) {
                if (self.currentView.get('topology') === parseInt(option.value)) {
                    option.selected = true;
                }
            });
            this.$('#graph-view-select option').each(function (i, option) {
                if (self.currentView.id === parseInt(option.value)) {
                    option.selected = true;
                }
            });
            this.$('#filter-orphan-nodes').prop(
                'checked',
                this.currentView.get('display_orphans')
            );

            _.each(this.currentView.get('categories'), function (category) {
                self.$('#filter-' + category).prop('checked', true);
            });
            window.onunload = function () {
                _.each(self.currentView.get('categories'), function (category) {
                    self.$('#filter-' + category).prop('checked', false);
                });
                self.$('#filter-orphan-nodes').prop(
                    'checked',
                    self.currentView.get('display_orphans')
                );
            };
        },

        toggleNetmapViewPanel: function (e) {

            this.$(e.currentTarget.children).toggleClass('fa-caret-down fa-caret-up');
            this.netmapViewPanel.toggle();
        },

        toggleAdvancedOptionsPanel: function (e) {

            this.$(e.currentTarget.children).toggleClass('fa-caret-down fa-caret-up');
            this.advancedOptionsPanel.toggle();
        },

        /**
         * Triggers when the topology layer is changed. Updates the
         * view and fires an event to the graph model
         * @param e
         */
        changeTopologyLayer: function (e) {

            var layer = e.currentTarget.value;
            this.currentView.set('topology', layer);
            Backbone.EventBroker.trigger('netmap:topologyLayerChanged', layer);
        },


        /**
         * Triggers when the current netmap view is changed
         * @param e
         */
        changeNetmapView: function (e) {

            var viewId = e.currentTarget.value;
            this.currentView = this.netmapViews.get(viewId);

            var newCategories = this.currentView.get('categories');
            _.each(this.$('.filter-category'), function (elem) {
                elem.checked = _.contains(newCategories, elem.value);
            });
            this.$('#filter-orphan-nodes').prop(
                'checked',
                this.currentView.get('display_orphans')
            );

            Backbone.EventBroker.trigger('netmap:netmapViewChanged', this.currentView);
        },

        /**
         * Triggers when a new category is selected. Updates the
         * current view and notifies the graph.
         * @param e
         */
        updateCategoryFilter: function (e) {

            var categoryId = e.currentTarget.value;
            var checked = e.currentTarget.checked;
            var categories = this.currentView.get('categories');

            if (checked) {
                categories.push(categoryId);
            } else {
                categories.splice(categories.indexOf(categoryId), 1);
            }

            Backbone.EventBroker.trigger('netmap:filterCategoriesChanged', categoryId, checked);
        },


        updateOrphanNodesFilter: function (e) { console.log('Orphans');

            this.currentView.set('display_orphans', e.currentTarget.checked);

            Backbone.EventBroker.trigger('netmap:updateGraph');
        },


        saveCurrentView: function () {

            // Update `display_elinks` and remove 'ELINKS' from categories if present
            var categories = this.currentView.get('categories');
            this.currentView.set('display_elinks', _.indexOf(categories, 'ELINK') >= 0);
            this.currentView.set('categories', _.without(categories, 'ELINK'));
            this.currentView.set('last_modified', new Date());

            var self = this;
            this.currentView.save(this.currentView.attributes,
                {
                    success: function () {
                        self.saveSuccessful.call(self);
                        Backbone.EventBroker.trigger('netmap:saveNodePositions');
                    },
                    error: function () {
                        self.saveError.call(self);
                    }
                }
            );
        },

        /**
         * Triggers a graph search for the given query
         * @param e
         */
        searchGraph: function (e) {
            e.preventDefault();
            var query = $('#graph-search-input', e.currentTarget).val();
            Backbone.EventBroker.trigger('netmap:netmapGraphSearch', query);
        },

        /* Save callbacks */

        saveSuccessful: function () {

            var alert = this.alertContainer.html('<span class="alert-box success">View saved successfully</span>');
            setTimeout(function () {
                $('span', alert).fadeOut(function () {
                    this.remove();
                });
            }, 3000);
        },

        saveError: function () {

            var alert = this.alertContainer.html(
                '<span class="alert-box alert">Save unsuccessful!' +
                    '<a href="#" class="close">&times;</a></span>'
            );
            $('span a', alert).click(function () {
                $('span', alert).fadeOut(function () {
                    this.remove();
                }) ;
            });
        }
    });

    return ControlView;
});