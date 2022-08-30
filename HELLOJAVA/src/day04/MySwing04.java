package day04;

import java.awt.EventQueue;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;



public class MySwing04 extends JFrame {

	private JPanel contentPane;
	private JLabel label2;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing04 frame = new MySwing04();
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
	public MySwing04() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel label1 = new JLabel("-");
		label1.setBounds(12, 59, 47, 15);
		contentPane.add(label1);
		
		label2 = new JLabel("-");
		label2.setBounds(82, 59, 47, 15);
		contentPane.add(label2);
		
		JLabel label3 = new JLabel("-");
		label3.setBounds(159, 59, 47, 15);
		contentPane.add(label3);
		
		JLabel label4 = new JLabel("-");
		label4.setBounds(230, 59, 47, 15);
		contentPane.add(label4);
		
		JLabel label5 = new JLabel("-");
		label5.setBounds(301, 59, 47, 15);
		contentPane.add(label5);
		
		JLabel label6 = new JLabel("-");
		label6.setBounds(375, 59, 47, 15);
		contentPane.add(label6);
		
		JButton btn = new JButton("로또생성하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				
				Set<Integer> listSet = new HashSet<Integer>();
				
				while( listSet.size() <= 6 ) {
					
					int n = ( int ) ( Math.random() * 45 ) + 1;
					
					listSet.add( n );
					
				}
				
				
				List<Integer> numbers = new ArrayList<>(listSet);
				
				label1.setText( numbers.get( 0 ) + "" );
				label2.setText( numbers.get( 1 ) + "" );
				label3.setText( numbers.get( 2 ) + "" );
				label4.setText( numbers.get( 3 ) + "" );
				label5.setText( numbers.get( 4 ) + "" );
				label6.setText( numbers.get( 5 ) + "" );
				
				
			}
		});
		btn.setBounds(45, 110, 133, 23);
		contentPane.add(btn);
	}

	
	
	
	
}
