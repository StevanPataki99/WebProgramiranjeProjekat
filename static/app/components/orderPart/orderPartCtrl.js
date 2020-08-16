(function(angular){

    var app = angular.module("app");


    app.controller("orderPartCtrl", ["$http" , "$state", "$stateParams", "$scope", function($http, $state, $stateParams, $scope) {
        var that = this;

        $scope.part_id = $stateParams['part_id'];
        $scope.user_id = $stateParams['user_id'];
        $scope.pices = $stateParams['pices'];
        $scope.price = null

        $scope.user = null;
        $scope.part = null;

        $scope.order_date = null;
        
        console.log($scope.order_date)

        console.log($stateParams['part_id'])
        console.log($stateParams['user_id'])
        console.log($stateParams['pices'])

        $scope.form_data = [
            {"order_date" : $scope.order_date, "order_price" : "", "order_status" : ""},
            {"country_name" : "", "city_name" : "", "adress_street" : "", "adress_number" : ""},
            {"user_id" : "", "part_id" : "", "pices" : ""}
        ]

        this.getPart = function(part_id) {
            $http.get("api/part/" + part_id).then(function(result){
                console.log(result);
                $scope.part = result.data[0];
                $scope.price = result.data[0]["part_price"] * $scope.pices
                console.log($scope.part);
                console.log($scope.price);

            },
            function(reason){
                console.log(reason);
            })
        }

        this.getUser = function(user_id) {
            $http.get("api/user/" + user_id).then(function(result){
                console.log(result);
                $scope.user = result.data[0];
                console.log($scope.user);
            },
            function(reason){
                console.log(reason);
            })
        }

        this.order = function() {
            $scope.form_data[0]["order_date"] = $scope.order_date;
            $scope.form_data[0]["order_price"] = $scope.part["part_price"] * $scope.pices;
            $scope.form_data[0]["order_status"] = "ORDERD";
            $scope.form_data[2]["user_id"] = $scope.user_id;
            $scope.form_data[2]["part_id"] = $scope.part_id;
            $scope.form_data[2]["pices"] = $scope.pices;
            console.log($scope.form_data);
            window.alert("Here we will simulate filling out youre credit card details");
            that.sendOrder();
        }

        this.sendOrder = function() {
            $http.post("api/order", $scope.form_data).then(function(result){
                console.log(result);
                window.alert("Order successful!")
                $state.go("home")

            },
            function(reason){
                console.log(reason);
                window.alert("Order failed")
            })
        }

        this.formDate = function() {
            finall_date = "";
            date = new Date();
            
            finall_date = finall_date + date.getFullYear() + "-";
            if (date.getMonth() < 10){
                finall_date = finall_date + "0" + date.getMonth() + "-";
            }else{
                finall_date = finall_date + date.getMonth + "-";
            }

            if (date.getDay() < 10){
                finall_date = finall_date + "0" + date.getDay();
            }else{
                finall_date = finall_date + date.getDay();
            }

            console.log(finall_date);
            $scope.order_date = finall_date;
        }

        this.formDate();
        this.getPart($scope.part_id);
        this.getUser($scope.user_id);

    }]);
})(angular);