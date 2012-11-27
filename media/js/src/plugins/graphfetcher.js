define(['libs/jquery'], function () {
    /*
     * GraphFetcher
     *
     * Usage: new GraphFetcher(node, url, [config])
     *
     * node - jQuery element to work in
     * url - url to use when fetching graph-url
     * config - object containing options. (currently only image title)
     *
     * NAV's rrdgrapher returns an url when creating a graph. GraphFetcher
     * fetches that url with ajax, creates an image and puts the url as source
     *
     * In addition GraphFetcher adds some parameters to the request that may
     * be used to modify the graph.
     *
    */

    function GraphFetcher(node, url, config) {
        this.checkInput(node, url);
        this.node = node;
        this.url = url;
        this.config = config;

        this.buttons = {'day': 'Day', 'week': 'Week', 'month': 'Month', 'year': 'Year'};

        this.addButtons();
        this.loadGraph('day');
    }

    GraphFetcher.prototype = {
        checkInput: function (node, url) {
            if (!(node instanceof jQuery && node.length)) {
                throw new Error('Need a valid node to attach to');
            }
            if (!(typeof url === "string")) {
                throw new Error('Need a string as url');
            }
        },
        addButtons: function () {
            var headerNode = $('<div/>').appendTo(this.node);
            this.headerNode = headerNode;

            for (var key in this.buttons) {
                if (this.buttons.hasOwnProperty(key)) {
                    this.addButton(headerNode, key, this.buttons[key]);
                }
            }
        },
        addButton: function (node, timeframe, text) {
            var that = this;
            var button= $('<button />').addClass('graph-button-' + timeframe).html(text);
            button.click(function () {
                that.loadGraph(timeframe);
            });
            button.appendTo(node);
        },
        selectButton: function(timeframe) {
            $('button', this.headerNode).each(function (index, element) {
                $(element).removeClass('button-selected');
            });
            $('button.graph-button-' + timeframe, this.node).addClass('button-selected');
        },
        loadGraph: function (timeframe) {
            var that = this;
            var jqxhr = $.get(this.url, {'timeframe': timeframe}, function (data) {
                that.displayGraph(data.url);
                that.selectButton(timeframe);
            });
            this.handleXhr(jqxhr);
        },
        displayGraph: function (url) {
            var title = this.config.title || '';
            var attrs = {
                'src': url,
                'title': title
            };

            if ($('img', this.node).length > 0) {
                $('img', this.node).attr('src', url);
            } else {
                $('<img/>').attr(attrs).appendTo(this.node);
            }
        },
        handleXhr: function (xhr) {
            var that = this;
            xhr.fail(function () {
                if (!$('span.error', that.node).length) {
                    $('<span class="error"/>').text('Failed to load graph').appendTo(that.node);
                }
            });
            xhr.done(function () {
                $('span.error', that).remove();
            })
        }
    };

    return GraphFetcher;

});
