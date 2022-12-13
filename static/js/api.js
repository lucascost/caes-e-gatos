const URL_UF = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados/'
const UF = document.getElementsByName('estado')
const CIDADES = document.getElementsByName('cidade')


UF.forEach((field) => {
    field.addEventListener('change', async () => {
        CIDADES.forEach((cidade) => cidade.innerHTML = '<option value""></option>')
        let url = URL_UF + field.value + '/municipios'
        const request = await fetch(url)
        const response = await request.json()

        response.forEach((cidade) => {
            CIDADES.forEach((field) => field.innerHTML += `<option>${cidade.nome}</option>`);
        })
    })
})
window.addEventListener('load', async () => {
    const request = await fetch(URL_UF)
    const response = await request.json()
    let ufs = response.sort((a, b) => (a.sigla > b.sigla ? 1 : -1))

    UF.forEach((field) => {
        ufs.forEach((uf) => {
            field.innerHTML += `<option value="${uf.sigla}">${uf.nome}</option>`
        })
    })

})
