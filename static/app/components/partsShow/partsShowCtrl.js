(function(angular){

    var app = angular.module("app");


    app.controller("partsShowCtrl", ["$http" , "$state","$scope", function($http, $state, $scope) {
        var that = this;

        $scope.parts = []; 
        this.getParts = function() {
            $http.get("api/parts").then(function(result){
                console.log(result);
                $scope.parts = result.data;
                console.log($scope.parts)
            },
            function(reason) {
                console.log(reason);
            });
        }

        this.getPartsPriceUp = function() {
            $http.get("api/partsPriceUp").then(function(result){
                $scope.parts = [];
                console.log(result);
                $scope.parts = result.data;
            },
            function(reason) {
                console.log(reason);
            });
        }

        this.getPartsPriceDown = function() {
            $http.get("api/partsPriceDown").then(function(result){
                $scope.parts = [];
                console.log(result);
                $scope.parts = result.data;
            },
            function(reason) {
                console.log(reason);
            });
        }

        this.getPartsPriceAbc = function() {
            $http.get("api/partsPriceAbc").then(function(result){
                $scope.parts = [];
                console.log(result);
                $scope.parts = result.data;
            },
            function(reason) {
                console.log(reason);
            });
        }

        this.searchParts = function() {
            $http.get("api/partSearch/" + $scope.searchValue).then(function(result){
                console.log(result);
                $scope.parts = result.data;
                console.log($scope.parts)
            },
            function(reason) {
                console.log(reason);
            });
        }

        this.getParts();

    }]);
})(angular);