var app = app || {};

app.TaskDeckView = Backbone.View.extend({
    el: '#task-table',
    initialize: function( initialTasks ) {
        this.collection = new app.TaskDeck( initialTasks );
        this.render();
    },
    render: function() {
        this.collection.each(function( item ) {
            this.renderTask( item );
        }, this );
    },
    renderTask: function( item ) {
        var taskView = new app.TaskView({
            model: item
        });
        this.$el.append( taskView.render().el );
    }
});
