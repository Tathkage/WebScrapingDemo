import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module'; // If using routing
import { AppComponent } from './app.component';
import { AnimeListComponent } from './anime-list/anime-list.component';
import { HttpClientModule } from '@angular/common/http';


@NgModule({
  declarations: [
    AppComponent,
    AnimeListComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule // If using routing
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
