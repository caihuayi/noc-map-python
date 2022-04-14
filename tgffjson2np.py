import json
import os
import argparse

def tgffjson2np(path):
  edges = []
  with open(path, 'r') as f:
    content = f.read()
    tgff = json.loads(content)
    for edge in tgff['edges']:
      # print(edge)
      dst = int(edge['to'].split('_')[1])
      src = int(edge['from'].split('_')[1])
      print(str(dst) + ' ' + str(src))
      edges.append([dst, src])
    
  return edges

def main():
    path = '/home/caihuayi/lab/tgff-3.6/examples/kbasic_task.json'
    edges = tgffjson2np(path)
    print (edges)

if __name__ == '__main__':
    main()
