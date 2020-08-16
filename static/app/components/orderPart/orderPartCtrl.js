(function(angular){

    var app = angular.module("app");


    app.controller("orderPartCtrl", ["$http" , "$state", "$stateParams", "$scope", function($http, $state, $stateParams, $scope) {
        var that = this;

        $scope.part_id = $stateParams['part_id'];
        $scope.user_id = $stateParams['user_id'];
        $scope.pices = $stateParams['pices'];

        console.log($stateParams['part_id'])
        console.log($stateParams['user_id'])
        console.log($stateParams['pices'])
        

    }]);
})(angular);