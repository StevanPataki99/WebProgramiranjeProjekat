(function(angular){

    var app = angular.module("app");


    app.controller("logInCtrl", ["$http" , "$state", "$stateParams", "$scope", function($http, $state, $stateParams, $scope) {
        var that = this;

        this.user = {
            "email" : "",
            "password" : ""
        };

        this.logIn = function() {
            $http.post("api/userLogIn", that.user).then(function(result){
                console.log(result);
                window.alert("User successfully loged in.")
                $state.go("home");
            },
            function(reason){
                console.log(reason);
                window.alert("Something wen wrong! User did not log in try again.")
            })
        }

    }]);
})(angular);