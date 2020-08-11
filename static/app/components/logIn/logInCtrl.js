(function(angular){

    var app = angular.module("app");


    app.controller("logInCtrl", ["$http" , "$state", "$stateParams", "$scope", function($http, $state, $stateParams, $scope) {
        var that = this;

        this.part = [];

        this.getPart = function(part_id) {
            $http.get("api/part/" + part_id).then(function(result){
                console.log(result);
                that.part = result.data;
            },
            function(reason){
                console.log(reason);
            })
        }

        $scope.order = function(){
            console.log("Ovde ide provera validnosti porudzbine")
            console.log($scope.pices)
        };
        

        // this.getPart($stateParams['part_id']);
        

    }]);
})(angular);