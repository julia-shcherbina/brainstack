var app = app || {};

app.TaskView = Backbone.View.extend({
    tagName: 'div',
    className: 'taskContainer',
    template: _.template($('#task-template').html()),
    render: function() {
        this.$el.html(this.template(this.model.toJSON()));
        return this;
    }
})
