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
        }).state({
            name: "logIn",
            url: "/logInCtrl",
            templateUrl: "app/components/logIn/Login.tpl.html",
            controller: "logInCtrl",
            controllerAs: "pctrl"
        }).state({
            name: "register",
            url: "/registerCtrl",
            templateUrl: "app/components/register/register.tpl.html",
            controller: "registerCtrl",
            controllerAs: "pctrl"
        })
        .state({
            name: "logout",
            url: "/logoutCtrl",
            templateUrl: "app/components/logout/logout.tpl.html",
            controller: "logoutCtrl",
            controllerAs: "pctrl"
        }).state({
            name: "userShow",
            url: "/userShowCtrl",
            templateUrl: "app/components/userShow/userShow.tpl.html",
            controller: "userShowCtrl",
            controllerAs: "pctrl"
        }).state({
            name: "userEdit",
            url: "/userEditCtrl/{user_id}",
            templateUrl: "app/components/userEdit/userEdit.tpl.html",
            controller: "userEditCtrl",
            controllerAs: "pctrl"
        }).state({
            name: "admin",
            url: "/adminCtrl",
            templateUrl: "app/components/admin/admin.tpl.html",
            controller: "adminCtrl",
            controllerAs: "pctrl"
        }).state({
            name: "editPart",
            url: "/editPartCtrl/{part_id}",
            templateUrl: "app/components/editPart/editPart.tpl.html",
            controller: "editPartCtrl",
            controllerAs: "pctrl"
        }).state({
            name: "newPart",
            url: "/newPartCtrl",
            templateUrl: "app/components/newPart/newPart.tpl.html",
            controller: "newPartCtrl",
            controllerAs: "pctrl"
        }).state({
            name: "about",
            url: "/aboutCtrl",
            templateUrl: "app/components/about/about.tpl.html",
            controller: "aboutCtrl",
            controllerAs: "pctrl"
        }).state({
            name: "orderPart",
            url: "/orderPartCtrl",
            templateUrl: "app/components/orderPart/orderPart.tpl.html",
            controller: "orderPartCtrl",
            controllerAs: "pctrl",
            params: {
                part_id: null,
                user_id: null,
                pices: null
            }
        })
        $urlRouterProvider.otherwise("/")
    }])
})(angular);