'use strict';

angular.module('brainApp.controllers', []).
  controller('ProjectIndexCtrl', ['$scope', '$log', '$http', '$rootScope',
    function($scope, $log, $http, $rootScope){
        $scope.tasks = [];
        $scope.addNewTask = function(){
          $scope.tasks.unshift($scope.new);
          $scope.new = {};
          $http.post('/api/tasks/', angular.toJson($scope.new)).success(function(resp){
            $log.info(resp);
            
            
          });
        }
      
     }]);
