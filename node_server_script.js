#!/bin/env node
/*
  INFO: To use this file, have your main file, with an express.js app started,
  call this file and its createRoutes function. E.g:

  // require the file
  var arch_sync = require(__dirname + '/arch-sync.js');
  // call the createRoutes function
  arch_sync.createRoutes(app);

*/
// connect to mongoose
var mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/archpackagesync');

exports.createRoutes = function (app){
  // create the database connection
  var db = mongoose.connection

  db.on('error', console.error.bind(console, 'connection error:'));
  db.once('open', function callback () {
    // db connection successfull
    var packageSchema = mongoose.Schema({
      username: String,
      pacman: String,
      aur: String
    });
    var Package = mongoose.model('Package', packageSchema)

    // extension from root
    ext = "/arch-sync";
    // create the routes
    app.get(ext + '/', function(req, res){
      res.send("Sorry. There is nothing here.");
    });
    // saving a package list
    app.post(ext + '/', function(req, res){
      // first delete any models with the same username
      Package.find({ username: req.body.username }).remove();
      // now save the new one
      var newpkglist = new Package(req.body);
      newpkglist.save(function (err, pkglist) {
        if(err){
          res.send("Unable to save data.");
        } else {
          var fullURL = req.protocol + "://" + req.get('host') + req.url + pkglist.username;
          res.send("Saved with username " + pkglist.username + ". Go to " + fullURL + " to download your packages.");
        }
      });
    });
    // downloading a package list
    app.get(ext + '/:username', function(req, res){
      // fetch username, exclude _id from the returned results
      Package.findOne({ username: req.params.username }, 'username pacman aur', function(err, pkglist){
        if(err || pkglist == null){
          res.send("Unable to fetch for username: " + req.params.username);
        } else {
          res.send(pkglist);
        }
      });
    });
  });
}