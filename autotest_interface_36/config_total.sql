CREATE TABLE `config_total` (
  `id` int(2) NOT NULL AUTO_INCREMENT,
  `key_config` varchar(128) DEFAULT NULL COMMENT '关键字名称',
  `value_config` text COMMENT '关键字值',
  `description` varchar(128) DEFAULT NULL COMMENT '关键字解释信息',
  `status` int(2) DEFAULT NULL COMMENT '配置文件状态，1-有效，0-无效',
  `create_time` timestamp NULL DEFAULT NULL,
  `update_time` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COMMENT='接口测试配置表';

INSERT INTO `config_total` VALUES ('name_export', '[\'getIpInfo\',\'baidu\']', '导出接口数据配置', 1, '2017-9-10 22:43:34', '2018-1-29 01:05:54');
INSERT INTO `config_total` VALUES ('exe_setup', '{\'getIpInfo\':{\'level_check\':[0,1],\'level_exe\':[0,1,2]}}', '执行接口的条件设置，{接口名称:{检查级别:[0,1],执行级别:[0,1,2],执行环境:test}}。检查级别中[0,1]代表code和参数完整性检查，执行级别中[0,1]分别代表BVT，1级用例', 1, '2017-9-10 20:43:09', '2018-1-2 01:21:52');

CREATE TABLE config_total (
id int(2) NOT NULL AUTO_INCREMENT primary key,
key_config varchar(128) DEFAULT NULL,
value_config text,
description varchar(128) DEFAULT NULL,
status int(2) DEFAULT NULL,
create_time timestamp NULL DEFAULT CURRENT_TIMESTAMP,
update_time timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
)ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

INSERT INTO config_total (
key_config, value_config, description, status)
VALUES ('test', 'value_test', '测试配置', '1');

