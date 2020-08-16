(function(angular){

    var app = angular.module("app");


    app.controller("orderPartCtrl", ["$http" , "$state", "$stateParams", "$scope", function($http, $state, $stateParams, $scope) {
        var that = this;

        this.part_id = $stateParams['part_id'];
        this.user_id = $stateParams['user_id'];
        this.pices = $stateParams['pices'];

        console.log($stateParams['part_id'])
        console.log($stateParams['user_id'])
        console.log($stateParams['pices'])
        

    }]);
})(angular);