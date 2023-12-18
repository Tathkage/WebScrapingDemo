import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

interface Anime {
  title: string;
  rating: number;
}

@Component({
  selector: 'app-anime-list',
  templateUrl: './anime-list.component.html',
  styleUrls: ['./anime-list.component.css']
})
export class AnimeListComponent implements OnInit {
  animeList: Anime[] = [];

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.getAnimeList();
  }

  getAnimeList(): void {
    this.http.get<Anime[]>('http://localhost:8000/api/scrape-anime')
      .subscribe(data => {
        this.animeList = data;
      }, error => {
        console.error('There was an error!', error);
      });
  }
}
