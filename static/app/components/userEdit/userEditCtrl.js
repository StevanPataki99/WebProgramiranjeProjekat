(function (angular) {
    var app = angular.module("app");
    app.controller("userEditCtrl", ["$http", "$state", "$stateParams", function ($http, $state, $stateParams) {
        var that = this;

        this.getUser = function(user_id) {
            $http.get("api/user/" + user_id).then(function(result){ 
                that.newUser = result.data;
                console.log(that.newUser)
            }, function(reason) {
                console.log(reason);
            });
        }

        this.editUser = function(user_id) {
            $http.put("api/user/" + user_id, that.newUser).then(function(response) {
                console.log(response)
                window.alert("User info changed")
                $state.go("home");
            }, function(reason) {
                console.log(reason);
                
            });
        }

        this.save = function() {
            this.editUser($stateParams["user_id"]);
 
            
        }

        this.getUser($stateParams["user_id"]);

    }]);
})(angular);