


def MenuAdministrativo():
    print ("(4) Gestión de empresas")
     
    print ("(5) Gestión de transporte por empresa")

    print ("(6) Gestión de viaje")

    print ("(7) Consultar historial de reservaciones")

    print ("(8) Estadísticas de viaje")
    
    print ("(9) Retornar")

    
    opcion = input("Cual opcion desea selecciona: ")
    if isinstance(opcion,str):
        if (opcion=='4'):
            return GestionDeEmpresas()
            
        elif (opcion=='5'):
            return GestionDeTrasporteEmpresa()  
            
        elif (opcion=='6'):
            return GestionDeViaje()
                          
        elif (opcion=='7'):
            return ConsultarHistorialReservaciones()
          
        elif (opcion=='8'):
            return EstadisticaDeViaje()
        
        elif (opcion=='9'):
            return SistemaDeReservacion()
          
        else:
            print("Error, opcion incorrecta")

        print("\n")
        agendaContactos()



def MenuDelUsuario():
    print ("Seleccione una de las opciones a mostrar")
    
    print ("(10) Consulta de viajes")
    
    print ("(11) Reservación de viaje")
           
    print ("(12) Cancelación de reservación")
    
    print ("(13) Retornar")
    opcion = input("Cual opcion selecciona: ")
    if isinstance(opcion,str):
        if (opcion=='10'):
            (ConsultaDeViajes()) 
            
        elif (opcion=='11'):
            (ReservaciónDeViaje())
                                  
        elif (opcion=='12'):
            (CancelaciónDeReservación())
                  
        elif (opcion=='13'):
            (SistemaDeReservacion())
          
        else:
            print("Error, opcion incorrecta")


def SistemaDeReservacion():
    print("\n")
    print ("Seleccione una de las opciones a mostrar")
    print ("(1)    Opciones adminstrativas")
    print ("(2)    Opciones de usuario normal")
    print ("(3)    Salir")
    opcion = input("\nCual opcion desea seleccionar: ")

    if (opcion=='3'):
            return print("Hasta luego")

    if (isinstance(opcion,str)):
        if(opcion=='1'):
            (MenuAdministrativo())
            
        elif(opcion=='2'):
            (MenuDelUsuario()())
        
        else:
            print("Error, opcion incorrecta")


        print("\n")

SistemaDeReservacion()
