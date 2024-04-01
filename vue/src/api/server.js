import { request } from "../utils/request.js";
export function getCpuInfo() {
    return request({
      url: 'server/getCpuInfo',
      method: 'get',
    });
}
export function getCluster() {
  return request({
    url: 'server/getCluster',
    method: 'get',
  });
}
export function getMod() {
  return request({
    url: 'mod/getMain',
    method: 'get',
  });
}
export function getWorld() {
  return request({
    url: 'server/getWorld',
    method: 'get',
  });
}
export function getWorld2() {
  return request({
    url: 'server/getWorld2',
    method: 'get',
  });
}
export function getMessage(page_size,page_num,time_stamp) {
  return request({
    url: `message/${page_size}/${page_num}/${time_stamp}`,
    method: 'get',
  });
}
export function getActiveMessage() {
  return request({
    url: 'message',
    method: 'get',
  });
}
export function getUser() {
  return request({
    url: 'user',
    method: 'get',
  });
}