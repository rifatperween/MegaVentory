from tkinter import*
from PIL import Image,ImageTk     #for .jpg/.gif
from tkinter import ttk,messagebox
import sqlite3
class supplierClass():
    def __init__(self,root):
        
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Invertory Management System | Developed by Star Techies")
        self.root.config(bg="white")
        self.root.focus_force()
        # ============================
        # all variable
         
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        self.var_search=StringVar()
        self.var_desc=StringVar()

        # self.var_sup_id=StringVar()
        self.var_sup_invoice=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()

        
        # seachFrame
        self.root=LabelFrame(self.root,text="Search Employee",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        self.root.place(x=250,y=20,width=600,height=70)

        #option
        lbl_search=Label(self.root,textvariable=self.var_searchby,values=("Select","Email","Name","Contact"),state='readonly',justify=CENTER,bg="white",font=("goudy old style",15))
        lbl_search.place(x=10,y=10)
    

        txt_search=Entry(self.root,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(self.root,text="Search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=430,y=8,width=150,height=30)

        # title 
        title=Label(self.root,text="Supplier Details",font=("goudy old style",20, "bold"),bg="#0f4d7d",fg="white").place(x=50,y=10,width=1000, height=40)

        # content
        # row 1
        lbl_supplier_invoice=Label(self.root,text="Invoice No. ",font=("goudy old style",15),bg="white").place(x=50,y=150)
        txt_supplier_invoice=Entry(self.root,textvariable=self.var_sup_invoice,font=("goudy old style",15),bg="lightyellow").place(x=150,y=150,width=180)
       
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow").place(x=850,y=150,width=180)   
        # row 2
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=50,y=190)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=150,y=190,width=180)
        
        # row 3
        lbl_contact=Label(self.root,text="contact",font=("goudy old style",15),bg="white").place(x=50,y=230)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow").place(x=150,y=230,width=180)
       
        # row 4
        lbl_desc=Label(self.root,text="Description",font=("goudy old style",15),bg="white").place(x=50,y=270)
        
        self.txt_desc=Text(self.root,font= ("goudy old style",15),bg="lightyellow")
        self.txt_desc.place(x=180,y=200,width=470,height=90)
        
        # button
        btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=180,y=320,width=110,height=28)
        btn_update=Button(self.root,text="Upadte",command=self.update,font=("gpudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=300,y=320,width=110,height=35)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("gpudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=420,y=305,width=110,height=35)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("gpudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=540,y=320,width=110,height=35)

        # employee details
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=700,y=350,width=380,height=150)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.supplierTable=ttk.Treeview(emp_frame,columns=("invoice","name","contact","desc" ),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx(command=self.supplierTable.xview) 
        scrolly(command=self.supplierTable.yview) 

        self.supplierTable.heading("invoice",text="invoice no.")
        self.supplierTable.heading("name",text="NAME")
        self.supplierTable.heading("contact",text="CONTACT")
        self.supplierTable.heading("desc",text="description")
        self.supplierTable["show"]="heading"
        
        self.supplierTable.column("invoice",width=90)
        self.supplierTable.column("name",width=100)
        self.supplierTable.column("contact",width=100)
        self.supplierTable.column("desc",width=100)
        
        self.supplierTable.pack(fill=BOTH,expand=1)
        self.supplierTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()

#=============================================
    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error", "Invoice must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchnone()
                if row!=None:
                    messagebox.showererror("Error","Invoice no. already assigned, try different",parent=self.root)
                else:
                    cur.execute("Insert into supplier (invoice,name,contact,desc) values(?,?,?,?)",(
                                       self.var_sup_invoice.get(),
                                        self.var_name.get(),      
                                        self.var_contact.get(),
                                        self.var_desc.get(),
                                        
                    ))
                    con.commit()
                    messagebox.showinfo("Success","supplier Added Successfully",parent=self.root)
                    self.show()
        except Exception as  ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from supplier")
            rows=cur.fetchall()
            self.supplierTable.delete(*self.supplierTable.get_children())
            for row in rows:
               self.supplierTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)



    def get_data(self,ev):
        f=self.supplierTable.focus()
        content=(self.supplierTable.item(f))
        row=content['values']
        #print(row)
        self.var_sup_invoice.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])

        self.txt_desc.delete('1.0',END)
        self.txt_desc.insert(END,row[3])

 

    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error", "invoice no. must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchnone()
                if row==None:
                   messagebox.showererror("Error","Invalid invoice no.",parent=self.root)
                else:
                    cur.execute("Update supplier set name=?,contact=?,des=?, where invoice=?",(
                                    
                                        self.var_name.get(),                           
                                        self.var_contact.get(),
                                        self.txt_desc.get('1.0',END),                                  
                                       self.var_sup_invoice.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","supplier Updated Successfully",parent=self.root)
                    self.show()
        except Exception as  ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    
    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice no. must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid invoice no.",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                       cur.execute("delete from supplier where invoice=?",(self.var_sup_invoice.get(),))
                       con.commit()
                       messagebox.showinfo("Delete","supplier deleted Successfully",parent=self.root)
                       self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    
    def clear(self):
        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.txt_desc.delete('1.0',END)
        self.var_searchtxt.set()
        self.var_searchby.set("Select")
        self.show()

    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Invoice no. should be required",parent=self.root)

            else:
                cur.execute("select * from supplier where invoice =?" ,(self.var_searchtxt.get(),))
                row=cur.fetchone()
                if row==None:
                  self.supplierTable.delete(*self.supplierTable.get_children())
                  self.supplierTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

if __name__=="__main__":
    root=Tk()
    obj=supplierClass(root)
    root.mainloop()    

