(function (angular) {
    var app = angular.module("app");
    app.controller("editPartCtrl", ["$http", "$state", "$stateParams", function ($http, $state, $stateParams) {
        var that = this;

        this.getPart = function(part_id) {
            $http.get("api/part/" + part_id).then(function(result){ 
                that.newPart = result.data;
                console.log(that.newPart)
            }, function(reason) {
                console.log(reason);
            });
        }

        this.editPart = function(part_id) {
            console.log(part_id)
            console.log(that.newPart)
            $http.put("api/part/" + part_id, that.newPart).then(function(response) {
                console.log(response)
                window.alert("Part info changed")
                $state.go("home");
            }, function(reason) {
                console.log(reason);
                
            });
        }

        this.save = function() {
            if (that.newPart[0]['part_price'] === null || that.newPart[0]['part_price'] <= 0){
                window.alert("Enter vaild part price number!");
                return;
            }

            if (that.newPart[0]['part_stock'] === null || that.newPart[0]['part_stock'] < 0){
                window.alert("Enter vaild part stock number!")
                return;
            }

            if (that.newPart[0]['part_warranty'] === null || that.newPart[0]['part_warranty'] < 0){
                window.alert("Enter vaild part warranty number!");
                return;
            }

            this.editPart($stateParams["part_id"]);
 
            
        }

        this.getPart($stateParams["part_id"]);

    }]);
})(angular);