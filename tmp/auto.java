# 使用Mybatis读取oracle表AAAAPF中的所有记录，并将AAAAPF中的字段F1和F2写入到表BBBBPF中 

package com.example;

import java.io.FileInputStream;
import java.sql.Connection;
import java.sql.DriverManager;
import java.util.ArrayList;
import java.util.List;
import org.apache.ibatis.session.ExecutorType;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;
import com.example.domain.AAAAPF;
import com.example.domain.BBBBPF;

public class auto {
	public static void main(String[] args) throws Exception {
		// 加载mybatis的配置文件，这个文件就是上面提到的“xxx-config.xml” 
		FileInputStream in = new FileInputStream("d:\\project\\langchain_community_study\\tmp\\auto.xml");
		SqlSessionFactory sessionFactory = new SqlSessionFactoryBuilder().build(in);
		// 获取一个操作数据库的会话对象 
		SqlSession sqlSession = sessionFactory.openSession();
		Connection conn = sqlSession.getConnection();
		List<AAAAPF> aaaaPfList = new ArrayList<>();
		// 读取AAAAPF表中的所有记录 
		List<BBBBPF> bbbbPfList = new ArrayList<>();
		try {
			aaaaPfList = sqlSession.selectList("com.example.mapper.AAAAPFMapper.getAll");
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			sqlSession.commit();
			conn.close();
		}
		// 遍历AAAAPF表中的所有记录，并将其中的字段F1和F2写入到表BBBBPF中 
		try {
			sqlSession = sessionFactory.openSession(ExecutorType.BATCH);
			conn = sqlSession.getConnection();
			for (AAAAPF aaaaPf : aaaaPfList) {
				BBBBPF bbbbPf = new BBBBPF();
				bbbbPf.setF1(aaaaPf.getF1());
				bbbbPf.setF2(aaaaPf.getF2());
				sqlSession.insert("com.example.mapper.BBBBPFMapper.add", bbbbPf);
			}
			sqlSession.commit();
			conn.close();
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			sqlSession.close();
		}
	}
}

