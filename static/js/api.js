const URL_UF = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados/'
const UF = document.getElementById('uf')
const CIDADES = document.getElementById('cidade')

UF.addEventListener('change', async ()=>{
    CIDADES.innerHTML =''
    let url = URL_UF + UF.value + '/municipios'
    const request = await fetch(url)
    const response = await request.json()
    
    response.forEach((cidade)=>{
        CIDADES.innerHTML += `<option>${cidade.nome}</option>`
    })
})

window.addEventListener('load', async()=>{
    const request = await fetch(URL_UF)
    const response = await request.json()
    let ufs = response.sort((a, b) => (a.sigla > b.sigla ? 1 : -1))

    ufs.forEach((uf)=>{
        UF.innerHTML += `<option value="${uf.sigla}">${uf.nome}</option>`
    })
})