#!/usr/bin/env python
# encoding: utf-8
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from gstack import db


class AccessToken(db.Model):
    __tablename__ = 'accesstoken'
    access_token = db.Column(db.String(100), primary_key=True, unique=True)
    client_id = db.Column(db.String(100), unique=True)
    expires_in = db.Column(db.String(10))
    id_token = db.Column(db.String(1000))
    data = db.Column(db.String(500))

    def __init__(self, access_token, client_id, expires_in, id_token, data):
        self.access_token = access_token
        self.client_id = client_id
        self.expires_in = expires_in
        self.id_token = id_token
        self.data = data
