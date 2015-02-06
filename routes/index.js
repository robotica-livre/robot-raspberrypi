var express = require('express');
var router = express.Router();

var RaspiRobot = require("raspirobot").RaspiRobot, // Import the library
robot = new RaspiRobot();

robot.setup(); // Set up GPIO ports

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.get('/forward', function(req, res, next) {
	robot.setMotor("left", 1, 1);
	robot.setMotor("right", 1, 1);
});

router.get('/left', function(req, res, next) {
	robot.setMotor("left", 1, 0);
	robot.setMotor("right", 1, 1);
});

router.get('/down', function(req, res, next) {
	robot.setMotor("left", 1, 1);
	robot.setMotor("right", 1, 0);
});

router.get('/backward', function(req, res, next) {
	robot.setMotor("left", 1, 0);
	robot.setMotor("right", 1, 0);
});

module.exports = router;
