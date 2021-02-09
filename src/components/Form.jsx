
export default function Form() {
    const header = new Headers({
        'Accept': 'application/json',
      });
    //const data=JSON.stringify({nombre:'matias',apellido:'matt'});
    
    const enviarDatos = async (e) => {
        e.preventDefault();
        let formElement = document.getElementById("formdenuncia");
        let formulario = new FormData(formElement);
        //const data=JSON.stringify([formulario]);
        const request = await fetch("http://localhost:8000/cargadenuncia",{
        method : 'POST', 
        headers: header,
        body : formulario ,

    }) ;

    const response = await request.text();
    console.log(response);}

    return (
        <>



            <div class="container mt-5">
            <form id="formdenuncia" name = "formdenuncua" onSubmit={enviarDatos}>
                <div className="card mb-5">

                    <div className="card-header text-center">
                        Formulario de reporte de ciberdelito / incidente ante la <i>UECI</i>.
                    </div>
                    <div className="card-body">
                        

                            <div className="row d-flex justify-content-center">

                                <div className="col-md-4">

                                    <label htmlFor="Nombre">Nombre</label>
                                    <input type="text" name="nombre" id="nombre" className="form-control" />


                                </div>
                                <div className="col-md-4">

                                    <label htmlFor="Nombre">Apellido</label>
                                    <input type="text" name="apellido" id="apellido" className="form-control" />


                                </div>

                            </div>
                            <div className="row d-flex justify-content-center">

                                <div className="col-md-8">

                                    <label htmlFor="Nombre">Mail</label>
                                    <input type="text" name="mail" id="mail" className="form-control" />
                                </div>
                            </div>
                            <div className="row d-flex justify-content-center">

                                <div className="col-md-4">

                                    <label htmlFor="Nombre">Telefono</label>
                                    <input type="text" required name="telefono" id="telefono" className="form-control" />


                                </div>
                                <div className="col-md-4">
                                
                                    <label htmlFor="Nombre">Departamento</label>
                                    <select name="" className="form-control" id="departamento">
                                        <option>Departamento Sanagasta</option>
                                    </select>
                                </div>
                                </div>
                                
                                <div className="row d-flex justify-content-center">
                                    <div className="col-md-4">
                                        <label htmlFor="Nombre">Ciberdelito</label>
                                        <select name="" className="form-control" id="ciberdelito">
                                            <option>Goorming</option>
                                        </select>
                                    </div>

                                    <div className="col-md-4">
                                        <label htmlFor="Nombre">Incidente</label>
                                        <select name="" className="form-control" id="invidente">
                                            <option>Phishing</option>
                                        </select>
                                    </div>
                                    

                                </div>
                                <div className="row d-flex justify-content-center">

                                    <div className="col-md-4">

                                        <label htmlFor="Nombre">¿Realizo la denuncia?</label>
                                        <input type="checkbox" name="denuncia" id="denuncia" />


                                    </div>
                                    <div className="col-md-4">

                                        <label htmlFor="Nombre">Donde</label>
                                        <input type="text" name="lugarDeDenuncia" id="lugarDeDenuncia" className="form-control" />
                                    </div>


                                </div>
                                <div className="row d-flex justify-content-center">

                                    <div className="col-md-4 mt-4">

                                        <label htmlFor="Nombre">Plataforma</label>
                                        <select name="" className="form-control" id="plataforma">
                                            <option value="Facebook">Facebook</option>
                                        </select>


                                    </div>
                                    <div className="col-md-4">

                                        <label htmlFor="Nombre">Adjunte vinculo / URL/pagina web/perfil de red social/publicación a reportar</label>
                                        <input type="text" name="url_evidencia" id="url_evidencia" className="form-control" />
                                    </div>


                                </div>
                                <div className="row d-flex justify-content-center">

                                    <div className="col-md-4 ">

                                        <label htmlFor="Nombre">Imagenes</label>
                                        <input type="file" multiple name="imagenes" id="imagenes"/>


                                    </div>
                                    <div className="col-md-4">

                                        <label htmlFor="Nombre">observacion</label>
                                        <input type="text" name="observacion" id="observacion" className="form-control" />
                                    </div>

                                    
                                </div>

                        
                        

                    </div>
                    <div className="card-footer d-flex justify-content-center">
                        <button type="submit" onClick={enviarDatos} className="btn btn-success">Guardar</button>

                    </div>
                </div>
                </form>
            </div>


        
        </>
    )
}