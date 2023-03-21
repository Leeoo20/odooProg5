odoo.define('students.student_view_form', function (require) {
    "use strict";

    console.log('count.js loaded');

    var core = require('web.core');
    var Widget = require('web.FormRenderer');


    var MyPage = Widget.extend({
        template: 'students.student_view_form',
        events: {
            'click .o_call_button_prueba': '_onButtonClicked',
        },
        init: function (parent, state, params) {
            this._super.apply(this, arguments);
            console.log('init count');
        },
        _onButtonClicked: function(ev) {
            ev.preventDefault();
            console.log('Button clicked!');
        },
    });

    core.action_registry.add('students.student_view_form', MyPage);

    return MyPage;
});