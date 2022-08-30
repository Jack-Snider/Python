package day05;

import java.awt.EventQueue;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import javax.swing.border.EmptyBorder;

public class MySwing07 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing07 frame = new MySwing07();
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
	public MySwing07() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 272, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("단수 :");
		lbl.setBounds(12, 28, 57, 15);
		contentPane.add(lbl);
		
		tf = new JTextField();
		tf.setBounds(81, 25, 132, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JTextArea ta = new JTextArea();
		ta.setBounds(12, 86, 201, 165);
		contentPane.add(ta);
		
		JButton btn = new JButton("출력하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				
				try {
					
					int number = Integer.parseInt( tf.getText() );
					
					String str = "";
					
					for( int i = 1; i <= 9; i++ ) {
						str += number + " x " + i + " = " + ( number * i ) + "\n";
					}
					
					ta.setText( str );
					tf.setText( "" );
					
					
				}catch( NumberFormatException ne ) {
					System.out.println( "Error : Unacceptable Input" );
					ta.setText( "WARNING : Unvalid input" );
					
					
				}
				
				
				
			}
		});
		btn.setBounds(62, 53, 97, 23);
		contentPane.add(btn);
	}
}
