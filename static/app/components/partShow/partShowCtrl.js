(function(angular){

    var app = angular.module("app");


    app.controller("partShowCtrl", ["$http" , "$state", "$stateParams", "$scope", function($http, $state, $stateParams, $scope) {
        var that = this;

        this.part = [];
        this.user = null;

        this.getPart = function(part_id) {
            $http.get("api/part/" + part_id).then(function(result){
                console.log(result);
                that.part = result.data;
            },
            function(reason){
                console.log(reason);
            })
        }

        this.getUser = function() {
            $http.get("api/currentUser").then(function(result){
                console.log(result);
                that.user = result.data;
            },
            function(reason){
                console.log(reason);
            })
        }

        $scope.order = function(){
            console.log($scope.pices);
            console.log(that.user)

            if (that.user === null){
                window.alert("Cant order if not loged in!");
                return;
            }

            if ($scope.pices === undefined || $scope.pices <= 0){
                window.alert("Enter vaild amount number!");
                return;
            }

            if ($scope.pices > that.part[0]['part_stock']){
                window.alert("Your order is to large for current part stock!")
                return;
            }
            $state.go("orderPart", {part_id: that.part[0]['part_id'], user_id: that.user, pices: $scope.pices})

        };
        

        this.getPart($stateParams['part_id']);
        this.getUser();        

    }]);
})(angular);