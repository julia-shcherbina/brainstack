'use strict';

angular.module('brainApp', ['brainApp.controllers']).
  config(['$routeProvider', function($routeProvider) {
      $routeProvider.when('/', {
        templateUrl: '/static/js/project/tmpl/project-task-view.html',
        controller: 'ProjectIndexCtrl'
      });
      $routeProvider.otherwise({redirectTo: '/'});
  }]);