var app = app || {};

$(function () {
    var tasks = [
        { title: 'JavaScript: The Good Parts' },
        { title: 'The Little Book on CoffeeScript'},
        { title: 'Scala for the Impatient'},
        { title: 'American Psycho'},
        { title: 'Eloquent JavaScript',}
    ];

    new app.TaskDeckView( tasks );
});
