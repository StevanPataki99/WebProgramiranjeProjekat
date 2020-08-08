///<reference path="/Users/stevanpataki/Desktop/VezbaWebKol2/static/app/app.js">

(function(angular){

    var app = angular.module("app", ["ui.router"]);

    app.config(["$stateProvider", "$urlRouterProvider", function($stateProvider, $urlRouterProvider) {

        $stateProvider.state({
            name: "home",
            url: "/",
            templateUrl: "app/components/partsShow/partsShow.tpl.html",
            controller: "partsShowCtrl",
            controllerAs: "pctrl" 
        }).state({
            name: "korisnikPrikaz", 
            url: "/korisnikPrikaz/{id}",
            templateUrl: "app/components/korisnik-prikaz/korisnikPrikaz.tpl.html",
            controller: "korisnikPrikazCtrl",
            controllerAs: "pctrl"
        }).state({
            name: "partShow", 
            url: "/partShowCtrl/{part_id}",
            templateUrl: "app/components/partShow/partShow.tpl.html",
            controller: "partShowCtrl",
            controllerAs: "pctrl"
        })
        $urlRouterProvider.otherwise("/")
    }])
})(angular);