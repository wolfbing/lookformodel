// modules
var del = require('del'),
	gulp = require('gulp'),
	concat = require('gulp-concat'),
	imagemin = require('gulp-imagemin'),
	jshint = require('gulp-jshint'),
	minifycss = require('gulp-minify-css'),
	rename = require('gulp-rename'),
	uglify = require('gulp-uglify'),
	usemin = require('gulp-usemin'),
	pngcrush = require('imagemin-pngcrush');
	
// 压缩图片
gulp.task('img', function() {
	return gulp.src("static/images/bigImg/**/*")
    .pipe(imagemin({optimizationLevel: 7, progressive: true, use: [pngcrush()]}))
    .pipe(gulp.dest("static/images/img"));
});