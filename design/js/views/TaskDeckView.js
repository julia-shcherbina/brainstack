var app = app || {};

app.TaskDeckView = Backbone.View.extend({
    el: '#task-deck',
    initialize: function( initialTasks ) {
        this.collection = new app.TaskDeck();
        this.collection.fetch({reset: true});
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
        console.log(this.$el);
        this.$el.append( taskView.render().el );
    }
});
