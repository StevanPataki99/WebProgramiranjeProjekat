(function(angular){

    var app = angular.module("app");


    app.controller("logoutCtrl", ["$http" , "$state", "$stateParams", "$scope", function($http, $state, $stateParams, $scope) {
        var that = this;

        this.currentUser = null

        this.logout = function() {
            $http.get("api/logout").then(function(result){
                console.log(result);
                window.alert("User successfully loged out.");
                $state.go("home");
            },
            function(reason){
                console.log(reason);
                window.alert("Something wen wrong! User did not log out try again.");
            })
        }
        
        this.checkCurrentUser = function() {
            $http.get("api/currentUser").then(function(result){
                console.log(result);
                that.currentUser = result.data;
                console.log(that.currentUser)
                if (that.currentUser != null) {
                    that.logout();
                }else{
                    $state.go("home");
                }
            },
            function(reason){
                console.log(reason);
            })
        }

        this.checkCurrentUser();

    }]);
})(angular);