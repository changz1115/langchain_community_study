// 下面代码什么作用？ 


/*
 * ========= GET/POST/DELETE demo =========
 *
 * import { RoleApi } from '@/api';
 *
 * try {
 *    const reqParams = { xx: xxx };
 *    await RoleApi.createRoleUser({ roleUsers: [reqParams] });
 * } catch(e) {
 *    console.error(e);
 *    // system will automatically pop up error message
 *    // you can also do some special handling here
 * }
 *
 */

/*
 * ======== Download excel demo =========
 *
 * import { downloadExcel } from '@/utils/utils';
 *
 * result = await RoleApi.downloadRoleUserTemplate();
 * downloadExcel(result.blob, result.fileName);
 */

import axios from '@/common/plugins/http/axios';

const authPrefix = '/api/system-auth';
const rolePrefix = '/api/system-admin';

export const RoleApi = {
  // GET Method
  getUserInfo(): Promise<{ roleUser: UserRoleInfo }> {
    return axios.get(`${authPrefix}/me`);
  },
  getRoleList(params: {
    roleCodes?: string[];
    keyword?: string;
    withRoleUsers?: boolean;
  }): Promise<{ roles: RoleDetailInfo[] }> {
    return axios.get(`${rolePrefix}/role/list`, { params });
  },
  // POST Method
  createRoleUser(params: {
    roleUsers: CreateRoleParams[];
    batch?: boolean;
  }): Promise<{ roleUser: UserRoleInfo }> {
    return axios.post(`${rolePrefix}/role-user/create`, params);
  },
  // DETELE Method
  deleteRoleUser(params: { roleCode: string; userCode: string }) {
    return axios.delete(`${rolePrefix}/role-user/delete`, { params });
  },
  // DOWNLOAD BLOB File
  downloadRoleUserExcel(params: RoleUserSearchParams): Promise<DownloadResult> {
    return axios.get(`${rolePrefix}/role-user/download`, { params, responseType: 'blob' });
  },
  downloadRoleUserTemplate(): Promise<DownloadResult> {
    return axios.get(`${rolePrefix}/role-user/template`, { responseType: 'blob' });
  },
};



