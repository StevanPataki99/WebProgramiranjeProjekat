(function(angular){

    var app = angular.module("app");


    app.controller("userShowCtrl", ["$http" , "$state", "$stateParams", "$scope", function($http, $state, $stateParams, $scope) {
        var that = this;

        $scope.userData = null;
        $scope.orders = null;
        $scope.ordersDone = null;

        this.getCurrentUserId = function() {
            $http.get("api/currentUser").then(function(result){
                console.log(result);
                that.user = result.data;
                if (that.user == null){
                    window.alert("No user loged in!")
                    $state.go("home");
                }else{
                    console.log(that.user);
                    that.getCurrentUserData();
                    that.getValidOrders();
                    that.getDoneOrders();
                }
            },
            function(reason){
                console.log(reason);
            })
        }

        this.getCurrentUserData = function(){
            $http.get("api/user/" + that.user).then(function(result){
                console.log(result);
                $scope.userData = result.data;
                console.log($scope.userData);
            },
            function(reason){
                console.log(reason);
            })
        }

        this.getValidOrders = function(){
            $http.get("api/order/" + that.user).then(function(result){
                console.log(result);
                $scope.orders = result.data;
                console.log($scope.orders);
            },
            function(reason){
                console.log(reason);
            })
        }

        this.getDoneOrders = function(){
            $http.get("api/orderDone/" + that.user).then(function(result){
                console.log(result);
                $scope.ordersDone = result.data;
                console.log($scope.ordersDone);
            },
            function(reason){
                console.log(reason);
            })
        }

        this.showadress = function(adress_id){
            $http.get("api/order_adress/" + adress_id).then(function(result){
                console.log(result);
                adress_orders = result.data;
                console.log(adress_orders);
                data_string = "Street: " + adress_orders[0]['adress_street_name'] + " Street Number: " + adress_orders[0]['adress_street_number'] + " City: " + adress_orders[1]['city_name'] + " Country: " + adress_orders[2]['country_name'];
                window.alert(data_string);
            },
            function(reason){
                console.log(reason);
            })
        }

        this.showpart = function(order_id){
            $http.get("api/order_parts/" + order_id).then(function(result){
                console.log(result);
                part_orders = result.data;
                console.log(part_orders);
                data_string = "Part: " + part_orders[1]['part_name'] + " Quantaty: " + (part_orders[0]['order_price'] / part_orders[1]['part_price']);
                window.alert(data_string);
            },
            function(reason){
                console.log(reason);
                window.alert("Unabel to show part because it is removed from the store")
            })
        }

        this.deleteorder = function(order_id){
            $http.delete("api/order/" + order_id).then(function(result){
                console.log(result);
                $state.reload();
            },
            function(reason){
                console.log(reason);
            })
        }

        this.getCurrentUserId();

    }]);
})(angular);