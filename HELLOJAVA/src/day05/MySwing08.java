package day05;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing08 extends JFrame {

	private JPanel contentPane;
	private JTextField user_tf;
	private JTextField com_tf;
	private JTextField res_tf;
	private JButton btn_reset;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing08 frame = new MySwing08();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MySwing08() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 295, 273);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel user_lbl = new JLabel("나 : ");
		user_lbl.setBounds(25, 36, 57, 15);
		contentPane.add(user_lbl);
		
		user_tf = new JTextField();
		user_tf.setBounds(116, 33, 116, 21);
		contentPane.add(user_tf);
		user_tf.setColumns(10);
		
		JLabel com_lbl = new JLabel("컴퓨터 : ");
		com_lbl.setBounds(25, 81, 57, 15);
		contentPane.add(com_lbl);
		
		com_tf = new JTextField();
		com_tf.setBounds(116, 78, 116, 21);
		contentPane.add(com_tf);
		com_tf.setColumns(10);
		
		JLabel res_lbl = new JLabel("결과 : ");
		res_lbl.setBounds(25, 129, 57, 15);
		contentPane.add(res_lbl);
		
		res_tf = new JTextField();
		res_tf.setBounds(116, 126, 116, 21);
		contentPane.add(res_tf);
		res_tf.setColumns(10);
		
		JButton btn = new JButton("게임하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				
				int n = ( int )( Math.random() * 3 );
				
				String[] options = { "가위", "바위", "보" };
				
				// 사용자가 입력한 값 가져옴
				String user = user_tf.getText();
				
				// 컴퓨터가 뽑은 픽
				String com = options[ n ];
				com_tf.setText( com );
				
				
				String result = "";
				
				
				if( user.equals( com ) ) {
					result = "무승부";
				}else if( user.equals( "가위" ) && com.equals( "바위" ) ) {
					result = "컴퓨터 승";
				}else if( user.equals( "가위" ) && com.equals( "보" ) ) {
					result = "사용자 승";
				}else if( user.equals( "바위" ) && com.equals( "가위" ) ) {
					result = "사용자 승";
				}else if( user.equals( "바위" ) && com.equals( "보" ) ) {
					result = "컴퓨터 승";
				}else if( user.equals( "보" ) && com.equals( "가위" ) ) {
					result = "컴퓨터 승";
				}else if( user.equals( "보" ) && com.equals( "바위" ) ) {
					result = "사용자 승";
				}
				
				res_tf.setText( result );
				
				
			}
		});
		btn.setBounds(83, 178, 97, 23);
		contentPane.add(btn);
		
		btn_reset = new JButton("초기화");
		btn_reset.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				
				res_tf.setText( "" );
				user_tf.setText( "" );
				com_tf.setText( "" );
				
			}
		});
		btn_reset.setBounds(83, 211, 97, 23);
		contentPane.add(btn_reset);
	}
}
