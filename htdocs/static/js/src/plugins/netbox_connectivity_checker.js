define(['libs/spin', 'libs/jquery'], function (Spinner) {

    /**
     * This plugin is only useful on the SeedDB add/edit netbox form.
     *
     * Should fill "Collected info" with values from hidden form elements
     * at page load.
     *
     * When button is clicked, sends a request for the read only data. If
     * the request is successful, "Collected info" is repopulated in addition
     * to the hidden elements. If not successful, an error message is
     * displayed.
     *
     */

    function Checker(ipchecker) {
        console.log('ConnectivityCheckerForNetboxes called');

        var form = $('#seeddb-netbox-form'),
            button = form.find('.check_connectivity');

        var writeAlertBox = createAlertBox(),
            readAlertBox = createAlertBox();

        var spinContainer = $('<span>&nbsp;</span>').css({ position: 'relative', left: '20px'}).insertAfter(button),
            spinner = new Spinner({ 'width': 3, length: 8, radius: 5, lines: 11 });

        /**
         * Fake nodes are the ones displayed to the user. Real nodes are the
         * ones the form posts.
         */
        var fakeSysnameNode = $('<label>Sysname<input type="text" disabled></label>'),
            fakeSnmpVersionNode = $('<label>Snmp version<input type="text" disabled></label>'),
            fakeTypeNode = $('<label>Type<input type="text" disabled></label>'),
            realSysnameNode = $('#id_sysname'),
            realSnmpVersionNode = $('#id_snmp_version'),
            realTypeNode = $('#id_type');

        $('#div_id_serial').before(fakeSysnameNode).before(fakeSnmpVersionNode).before(fakeTypeNode);

        setDefaultValues();

        button.on('click', function () {
            hideAlertBoxes();
            var ip_address = $('#id_ip').val().trim(),
                read_community = $('#id_read_only').val(),
                read_write_community = $('#id_read_write').val();

            if (!(ip_address && read_community)) {
                var message = "We need an IP-address and a read community to talk to the device.";
                if (read_write_community) {
                    message += " The read write community is not used for reading in NAV.";
                }
                reportError(readAlertBox, message);
                return;
            }

            spinner.spin(spinContainer.get(0));
            disableForm();

            var checkHostname = ipchecker.getAddresses();
            checkHostname.done(function () {
                if (ipchecker.isSingleAddress) {
                    checkConnectivity(ip_address, read_community, read_write_community);
                } else {
                    onStop();
                }
            });

        });

        function checkConnectivity(ip_address, read_community, read_write_community) {
            console.log('Checking connectivity');
            var request = $.getJSON(NAV.urls.get_readonly, {
                'ip_address': ip_address,
                'read_community': read_community,
                'read_write_community': read_write_community
            });
            request.done(onSuccess);
            request.error(onError);
            request.always(onStop);
        }

        function disableForm() {
            form.css({'opacity': '0.5', 'pointer-events': 'none'});
        }

        function enableForm() {
            form.css({'opacity': 'initial', 'pointer-events': 'initial'});
        }

        function createAlertBox() {
            var alertBox = $('<div class="alert-box"></div>').hide().insertAfter(button);
            alertBox.on('click', function () {
                $(this).hide();
            });
            return alertBox;
        }

        function setDefaultValues() {
            fakeSysnameNode.find('input').val(realSysnameNode.val());
            fakeSnmpVersionNode.find('input').val(realSnmpVersionNode.val());
            fakeTypeNode.find('input').val(realTypeNode.find('option:selected').html());
        }

        function setNewValues(data) {
            realSysnameNode.val(data.sysname);
            fakeSysnameNode.find('input').val(data.sysname);
            realSnmpVersionNode.val(data.snmp_version);
            fakeSnmpVersionNode.find('input').val(data.snmp_version);
            realTypeNode.val(data.netbox_type);
            fakeTypeNode.find('input').val(realTypeNode.find('option:selected').html());
            $('#id_serial').val(data.serial);
        }

        function reportWriteTest(write_test) {
            if (write_test.status === true) {
                reportSuccess(writeAlertBox, 'Write test was successful');
            } else {
                var failText = '<div>Write test failed';
                if (write_test.custom_error === 'UnicodeDecodeError') {
                    failText += ', perhaps because of non-ASCII characters in the system location field.';
                    failText += '<br><br>sysLocation: ' + write_test.syslocation;
                }
                failText += '.</div>';
                failText += '<div><br>Error message: ' + write_test.error_message + '</div>';
                reportError(writeAlertBox, failText);
            }
        }

        function onSuccess(data) {
            if (data.snmp_version) {
                reportSuccess(readAlertBox, 'Read test was successful');
                if (data.snmp_write_test) {
                    reportWriteTest(data.snmp_write_test);
                }
                setNewValues(data);
            } else {
                reportError(readAlertBox, 'Read test failed. Is the community string correct?');
            }

        }

        function onError() {
            reportError(readAlertBox, 'Error during SNMP-request');
        }

        function onStop() {
            spinner.stop();
            enableForm();
        }

        function reportError(alertBox, text) {
            alertBox.addClass('alert').removeClass('success').html(text);
            alertBox.show();
        }

        function reportSuccess(alertBox, text) {
            alertBox.addClass('success').removeClass('alert').html(text);
            alertBox.show();
        }

        function hideAlertBoxes() {
            readAlertBox.hide();
            writeAlertBox.hide();
        }

    }

    return Checker;

});