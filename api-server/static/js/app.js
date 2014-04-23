var myApp = angular.module('myApp', []);

myApp.controller('FileCtrl', ['$scope', '$http', function ($scope, $http) {


  // Crée un Object user
  $scope.file = {};

  // Nous voulons effectuer la requête
  // et obtenir le nom de l'utilisateur
  $http({
    method: 'GET',
    url: '//127.0.0.1:3000/api/v0/files'
  })
  .success(function (data, status, headers, config) {
    // Ici nous assignons cet utilisateur à
    // notre modèle existant !
    $scope.file = data;

  })
  .error(function (data, status, headers, config) {
   // Une erreur est survenue
  });
}]);


