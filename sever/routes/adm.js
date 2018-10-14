var express = require('express');
var router = express.Router();
// 实现与MySQL交互
var mysql = require('mysql');
var config = require('../model/config');
// 使用连接池，提升性能
var pool = mysql.createPool(config.mysql);
/* GET home page. */
router.get('/', function (req, res, next) {
  // res.render('adm', {title: '管理员'});
  if(req.session.username){
    res.render('adm',{username:req.session.username});
  }else{
    res.render('login');
  }
});
router.get('/logout', function(req, res, next){
  delete req.session.username;
  return res.render('login');
});

router.post('/delete', function (req, res, next) {
  var name1 = req.body.name1;//获取前台请求的参数
  pool.getConnection(function (err, connection) {
    var $sql1 = "select * from user where username=?";
    connection.query($sql1, [name1], function(err, result){
      console.log(result);
      var resultJson = result;
      if(resultJson.length === 0){
        result ={
          code: 300,
          msg: '该用户不存在于数据库中'
        };
        console.log(result);
        res.json(result);
        connection.release();
      }else{
        var $sql2 = "delete from user where username=? ";
        connection.query($sql2, [name1], function (err, result) {
        if (result) {
            result = {
              code: 200,
              msg: 'success'
            };
          } else {
            result = {
              code: 400,
              msg: '失败'
            };
          }
          res.json(result); // 以json形式，把操作结果返回给前台页面
          connection.release();
        });
      }
    });
  });
});
module.exports = router;
