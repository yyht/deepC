
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
# pylint: disable=invalid-name, unused-argument
#
# This file is part of DNN compiler maintained at 
# https://github.com/ai-techsystems/dnnCompiler
#
# Author:
# Date:

import os, sys

os.system("pip3 install onnx")
from onnx import *
sys.path.append("../../../python/parser")
from onnx_parser import *

op_name = 'Sigmoid'

nodes = []
nodes.append(helper.make_node("Sigmoid", ["0"], ["1"]))
inputs = [helper.make_tensor_value_info("0", TensorProto.FLOAT, (2, 3, 4))]
outputs = [helper.make_tensor_value_info("1", TensorProto.FLOAT, (2, 3, 4))]
graph = helper.make_graph(nodes, op_name+"_graph", inputs, outputs)
model = helper.make_model(graph)
onnx.checker.check_model(model)
t_prefix = "../testcases/" + op_name + "/" + op_name
g_prefix = "../gold_files/" + op_name
onnx.save(model, t_prefix+".onnx")
parse(t_prefix+".onnx", g_prefix+".sym", onnx_output_file=t_prefix+".txt")