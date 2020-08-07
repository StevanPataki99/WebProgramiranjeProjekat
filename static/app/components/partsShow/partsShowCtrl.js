(function(angular){

    var app = angular.module("app");


    app.controller("partsShowCtrl", ["$http" , "$state", function($http, $state) {
        var that = this;

        this.parts = []; 
        this.getParts= function() {
            $http.get("api/parts").then(function(result){
                console.log(result);
                that.parts = result.data;
            },
            function(reason) {
                console.log(reason);
            });
        }

        // this.ukloniKorisnika = function(id) {
        //     $http.delete("api/student/" + id).then(function(response){
        //         console.log(response);
        //         that.dobaviKorisnike();
        //     },
        //     function(reason){
        //         console.log(reason);
        //     });
        // }

        // this.dobaviPredmete= function() {
        //     $http.get("api/predmet").then(function(result){
        //         console.log(result);
        //         that.predmet = result.data;
        //     },
        //     function(reason) {
        //         console.log(reason);
        //     });
        // }

        // this.ukloniPredmet = function(id) {
        //     $http.delete("api/predmet/" + id).then(function(response){
        //         console.log(response);
        //         that.dobaviPredmete();
        //     },
        //     function(reason){
        //         console.log(reason);
        //     });
        // }

        this.getParts();
        // this.dobaviPredmete();

    }]);
})(angular);