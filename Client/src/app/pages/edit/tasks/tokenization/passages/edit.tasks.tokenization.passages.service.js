
/* Copyright (C) 2017 Omri Abend, The Rachel and Selim Benin School of Computer Science and Engineering, The Hebrew University. */
(function () {
    'use strict';

    angular.module('zAdmin.pages.edit.tasks.passages')
        .service('editTokenizationTaskPassagesService', editTokenizationTaskPassagesService);

    /** @ngInject */
    function editTokenizationTaskPassagesService(apiService) {

        var service = {
            Data:[],
            getEditTableStructure: function(){
                return apiService.edit.tasks.tokenization.passages.getPassagesTableStructure().then(function (res){return res.data});
            },
            getTableData: function(id){
                var _service = this;
                return apiService.passages.getPassagesTableData(id).then(function (res){
                    angular.copy(res.data.results, _service.Data);
                    return _service.Data
                });
            },
            get:function(key){
                if(!angular.isArray(this.Data[key]) && this.Data[key] != null){
                    return [this.Data[key]]
                }
                return this.Data[key]
            },
            set:function(key,obj,indexToInsert){
                if(angular.isArray(this.Data[key])){
                    indexToInsert == null ? this.Data[key].push(obj) : this.Data[key][indexToInsert] = obj;

                }else{
                    this.Data[key][0] = obj;
                }
            }
        };
        return service;
    }

})();