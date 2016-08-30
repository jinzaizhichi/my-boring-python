package main

import (
	"html/template"
	"io/ioutil"
	"log"
	"net/http"
	"os"
)

func checkError(err error) {
	if err != nil {
		logg("ERROR", err.Error())
	}
}

func logg(logtype, logtext string) {
	log.Printf("[%s] %s", logtype, logtext)
}

type Filer struct {
	filename    string
	filecontent string
}

func (f *Filer) checkExistsOrCreate() {
	if checkFileExists("templates/datafile/"+f.filename) == false {
		_, err := os.Create("templates/datafile/" + f.filename)
		checkError(err)
	}

}

func checkFileExists(filename string) bool {
	_, err := os.Stat(filename)
	return err == nil || os.IsExist(err)
}

func (f *Filer) WriteToFile() {
	binby := []byte(f.filecontent)
	err := ioutil.WriteFile("templates/datafile/"+f.filename, binby, 0666)
	checkError(err)
}

func (f *Filer) ReadFromFile() {
	ff, err := os.Open("templates/datafile/" + f.filename)
	checkError(err)
	nnn, err := ioutil.ReadAll(ff)
	checkError(err)
	f.filecontent = string(nnn)
}

type Viewer struct {
	Title   string
	Content string
}

type Editer struct {
	Filename string
	Content  string
}

func editerHandler(w http.ResponseWriter, r *http.Request) {
	var f Filer
	f.filename = r.URL.Query()["filenm"][0]
	f.checkExistsOrCreate()
	f.ReadFromFile()
	var edr Editer
	edr.Filename = f.filename
	edr.Content = f.filecontent
	t, err := template.ParseFiles("templates/models/edit_model.html")
	checkError(err)
	t.Execute(w, &edr)

}

func editHandler(w http.ResponseWriter, r *http.Request) {
	r.ParseForm()
	var f Filer
	f.filecontent = r.PostFormValue("txx")
	f.filename = r.PostFormValue("fn")
	f.checkExistsOrCreate()
	f.WriteToFile()
}

func viewerHandler(w http.ResponseWriter, r *http.Request) {
	var f Filer
	f.filename = r.URL.Query()["filenm"][0]
	f.ReadFromFile()
	var v Viewer
	v.Title = f.filename
	v.Content = f.filecontent
	t, err := template.ParseFiles("templates/models/view_model.html")
	checkError(err)
	t.Execute(w, &v)
}

func indexHandler(w http.ResponseWriter, r *http.Request) {
	t, err := template.ParseFiles("templates/models/index_model.html")
	checkError(err)
	t.Execute(w, nil)
}

func main() {
	http.HandleFunc("/arview", viewerHandler)
	http.HandleFunc("/save_file", editHandler)
	http.HandleFunc("/edit", editerHandler)
	http.HandleFunc("/", indexHandler)
	http.Handle("/markdown_to_html/", http.FileServer(http.Dir("templates")))
	http.ListenAndServe(":9590", nil)
}
