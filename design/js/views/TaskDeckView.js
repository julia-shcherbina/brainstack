var app  = app || {};

app.TaskDeckView = Backbone.View.extend({
    el: '#books',
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
        console.log(app);
        var taskView = new app.TaskView({
            model: item
        });
        this.$el.append( app.TaskView.render().el );
    }
})
