!function($) {
	angularAPP.controller('indexPicCtrl', function($scope) {
		$scope.models = [];
		for (var i = 0; i < 12; i++) {
			$scope.models.push({src: "/static/images/img/a.png"});
		}
	});
}(jQuery)