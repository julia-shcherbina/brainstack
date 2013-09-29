var app = app || {};

app.TaskView = Backbone.View.extend({
    tagName: 'div',
    className: 'taskContainer',
    template: _.template($('#task-template').html()),
    render: function() {
        console.log( this.model.get('title'));
        this.$el.html(this.template(this.model.toJSON()));
        console.log(this.el)
        return this;
    }
});
