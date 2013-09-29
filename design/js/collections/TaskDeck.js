var app = app || {};

app.TaskDeck = Backbone.Collection.extend({
    model: app.Task,
    url: '/api/tasks'
});
