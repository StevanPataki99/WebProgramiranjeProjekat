(function (angular) {
    var app = angular.module("app");
    app.controller("newPartCtrl", ["$http", "$state", "$stateParams", "$scope", function ($http, $state, $stateParams, $scope) {
        var that = this;

        this.newPart = {
            "part_name" : "",
            "part_price" : null,
            "part_stock" : null,
            "part_manufacturer" : "",
            "part_warranty" : null,
            "part_info" : "",
            "part_image" : null
        }



        this.addNewPart = function() {
            $http.post("api/part", that.newPart).then(function(response){
                $state.go("admin");

            },function(reason){
                console.log(reason);
            });

        }

        this.addNewPartImage = function() {
            $http({
                method: 'post',
                url: 'imageupload',
                data: that.imgData,
                headers: {'Content-Type': undefined},
               }).then(function successCallback(response) { 
                console.log(response);
               });
            }
              

        

        this.add = function() {

            if (that.newPart['part_price'] === null || that.newPart['part_price'] <= 0){
                window.alert("Enter vaild part price number!");
                return;
            }

            if (that.newPart['part_stock'] === null || that.newPart['part_stock'] <= 0){
                window.alert("Enter vaild part stock number!");
                return;
            }

            if (that.newPart['part_warranty'] === null || that.newPart['part_warranty'] <= 0){
                window.alert("Enter vaild part warranty number!");
                return;
            }


            that.imgData = new FormData();

            let files = document.getElementById('file').files[0];
    
            that.imgData.append('file',files);

            let fileName = files['name'];
            let fileExt = fileName.slice(-3);

            if (fileExt !== 'png') {
                window.alert("Select vaild part image format( PNG )!");
                return;
            }

            that.newPart['part_image'] = files['name'];

            console.log(that.newPart)

            that.addNewPartImage();

            that.addNewPart();

        }

    }]);
})(angular);