"use strict";

/***************************************************
 Provide support TamaTama
 ***************************************************/

var TamaTama = function () {
    WalkyConnection.call(this);

    this.databases = function () {
    // --------------------------------------------------
        var that = this;
        var sys = that.getObject('!');
        return sys.exec('databases');
    };

    this.login = function (databaseName,login,password) {
    // --------------------------------------------------
        var that = this;
        var sys = that.getObject('!');
        return sys.exec('login',[databaseName,login,password]);
    };

    this.getModel = function (modelName) {
    // --------------------------------------------------
        var that = this;
        var pooler = that.getObject('pool');
        return pooler.exec('get',[modelName]);
    };
};

TamaTama.prototype = Object.create(WalkyConnection.prototype);


