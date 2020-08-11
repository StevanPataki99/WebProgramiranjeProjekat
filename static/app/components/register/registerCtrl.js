(function(angular){

    var app = angular.module("app");


    app.controller("registerCtrl", ["$http" , "$state", "$stateParams", "$scope", function($http, $state, $stateParams, $scope) {
        var that = this;

        this.user = {
            "name" : "",
            "email" : "",
            "phonenumber" : "",
            "password" : "",
            "country" : "",
            "city" : "",
            "streetName" : "",
            "streetNumber" : ""
        }

        this.register = function() {
            $http.post("api/user", that.user).then(function(result){
                console.log(result);
                window.alert("User successfully registerd")
                $state.go("logIn");
            },
            function(reason){
                console.log(reason);
                window.alert("User not registerd")
            })
        }


    }]);
})(angular);